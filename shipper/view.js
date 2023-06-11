const Shipper = require('../models/shipper');
const Order = require('../models/order');
const OrderDetails = require('../models/orderDetails');
const ShipperSerializer = require('../serializers/shipperSerializer');
const { get_user_for_request } = require('../common/utility/authentication_service');

const SUCCESS = 'Success';
const FAIL = 'Fail';
const TYPE = 'type';
const SHIPPERS = 'shippers';
const ORDER_ID = 'order_id';
const TOTAL_CHECKPOINTS = 'totalCheckpoint';
const CHECKPOINT = 'checkpoint';
const CURRENT_CHECKPOINT = 'currentCheckpoint';
const TRACKING_URL = 'trackingUrl';
const URL_STATUS = 'urlStatus';
const COMPANY_NAME = 'companyName';
const UPDATE = 'update';

exports.getShipper = async (req, res) => {
  const user = get_user_for_request(req);

  try {
    const orderDetails = await OrderDetails.findOne({
      'product.shop.userProfile': user,
      order_id: req.params.id,
    }).populate('order.shipper');

    if (!orderDetails || !orderDetails.order.shipper) {
      return res.status(404).json({ message: FAIL });
    }

    const serializedShipper = ShipperSerializer(orderDetails.order.shipper);
    const shipper = JSON.parse(JSON.stringify(serializedShipper));

    return res.status(200).json({ message: SUCCESS, shipper });
  } catch (error) {
    console.error(error);
    return res.status(500).json({ message: FAIL });
  }
};

exports.createShipper = async (req, res) => {
  const data = req.body;

  if (!data[SHIPPERS]) {
    return res.status(400).json({ message: FAIL });
  }

  const user = get_user_for_request(req);

  try {
    for (const shipperData of data[SHIPPERS]) {
      if (
        !shipperData[TYPE] ||
        !shipperData[ORDER_ID] ||
        !shipperData[COMPANY_NAME]
      ) {
        return res.status(400).json({ message: FAIL });
      }

      const orderDetails = await OrderDetails.findOne({
        'product.shop.userProfile': user,
        order_id: shipperData[ORDER_ID],
      });

      if (!orderDetails) {
        return res.status(404).json({ message: FAIL });
      }

      let newShipper;

      if (shipperData[TYPE] === 0) {
        // Small Scale Seller
        if (
          !shipperData[TOTAL_CHECKPOINTS] ||
          !shipperData[CURRENT_CHECKPOINT] ||
          !shipperData[CHECKPOINT]
        ) {
          return res.status(400).json({ message: FAIL });
        }

        if (
          shipperData[TOTAL_CHECKPOINTS] <= 0 ||
          shipperData[CURRENT_CHECKPOINT] <= 0 ||
          shipperData[CHECKPOINT].length !== shipperData[TOTAL_CHECKPOINTS]
        ) {
          return res.status(400).json({ message: FAIL });
        }

        newShipper = await Shipper.create({
          type: shipperData[TYPE],
          companyName: shipperData[COMPANY_NAME],
          checkPoints: shipperData[CHECKPOINT],
          totalCheckPoints: shipperData[TOTAL_CHECKPOINTS],
          currentCheckPoint: shipperData[CURRENT_CHECKPOINT],
        });
      } else {
        // Large Scale Seller
        if (!shipperData[URL_STATUS] || !shipperData[TRACKING_URL]) {
          return res.status(400).json({ message: FAIL });
        }

        newShipper = await Shipper.create({
          type: shipperData[TYPE],
          companyName: shipperData[COMPANY_NAME],
          trackingUrl: shipperData[TRACKING_URL],
          urlStatus: shipperData[URL_STATUS],
        });
      }

      const order = orderDetails.order;
      order.shipper_id = newShipper._id;

      await Order.updateOne({ _id: order._id }, order);
    }

    return res.status(200).json({ message: SUCCESS });
  } catch (error) {
    console.error(error);
    return res.status(500).json({ message: FAIL });
  }
};

exports.updateShipper = async (req, res) => {
  const data = req.body;

  if (!data[UPDATE]) {
    return res.status(400).json({ message: FAIL });
  }

  const user = get_user_for_request(req);

  try {
    const orderDetails = await OrderDetails.findOne({
      'product.shop.userProfile': user,
      order_id: req.params.id,
    }).populate('order.shipper');

    if (!orderDetails || !orderDetails.order.shipper) {
      return res.status(404).json({ message: FAIL });
    }

    const shipper = orderDetails.order.shipper;

    if (shipper.type === 1) {
      return res.status(400).json({ message: FAIL });
    }

    shipper.currentCheckPoint = data[UPDATE];
    await shipper.save();

    return res.status(200).json({ message: SUCCESS });
  } catch (error) {
    console.error(error);
    return res.status(500).json({ message: FAIL });
  }
};
