const { DateTime } = require('luxon');
const { OrderDetails } = require('../path/to/order_details/model');
const { OrderDetailsSerializer } = require('../path/to/order_details/serializer');
const { get_user_for_request } = require('../path/to/common/utility/authentication_service');

const SUCCESS = 'Success';
const FAIL = 'Fail';

// API Functions
const getOrders = async (req, res) => {
  try {
    const user = get_user_for_request(req);
    const pk = req.params.pk;
    
    const orderDetails = await OrderDetails.find({ product_id: pk, 'product.shop.userProfile': user });
    
    if (orderDetails.length > 0) {
      const serializedOrderDetails = OrderDetailsSerializer(orderDetails, many: true);
      const orderDetailsData = JSON.parse(JSON.stringify(serializedOrderDetails));
      return res.status(200).json({ message: SUCCESS, order_details: orderDetailsData });
    }
    
    return res.status(200).json({ message: SUCCESS, order_details: {} });
  } catch (error) {
    return res.status(500).json({ message: FAIL });
  }
};

const updateOrders = async (req, res) => {
  try {
    const user = get_user_for_request(req);
    const data = req.body;

    if (!data.ids) {
      return res.status(400).json({ message: FAIL });
    }

    for (const id of data.ids) {
      const orderDetails = await OrderDetails.findOne({ _id: id, 'product.shop.userProfile': user });
      
      if (orderDetails && !orderDetails.shipedDate) {
        orderDetails.shipedDate = DateTime.now();
        await orderDetails.save();
      }
    }

    return res.status(200).json({ message: SUCCESS });
  } catch (error) {
    return res.status(500).json({ message: FAIL });
  }
};

module.exports = {
  getOrders,
  updateOrders,
};
