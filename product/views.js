const { json } = require('express');
const { IsAuthenticated, permission_classes, Response } = require('rest_framework');

const Product = require('../models/product');
const Shop = require('../models/shop');
const UserProfile = require('../models/userProfile');
const { get_user_for_request } = require('../common/utility/authentication_service');

const NAME = 'name';
const SUCCESS = 'Success';
const FAIL = 'Fail';
const SHOP_ID = 'shopId';
const SKU = 'sku';
const PRICE = 'price';
const DESCRIPTION = 'description';
const DISCOUNT = 'discount';
const UNIT_IN_STOCK = 'unitsInStock';
const SIZE = 'size';
const COLOUR = 'colour';
const UNIT_WEIGHT = 'unitWeight';
const IDS = 'ids';

exports.getProducts = async (req, res) => {
  const user = get_user_for_request(req);

  const { name } = req.query;
  const query = name ? { name, 'shop.userProfile': user } : { 'shop.userProfile': user };

  try {
    const products = await Product.find(query).lean();

    return res.status(200).json({ message: SUCCESS, products });
  } catch (error) {
    console.error(error);
    return res.status(500).json({ message: FAIL });
  }
};

exports.postProducts = async (req, res) => {
  const user = get_user_for_request(req);

  const { products } = req.body;

  if (!products) {
    return res.status(400).json({ message: FAIL });
  }

  try {
    for (const product of products) {
      const { name, shopId, sku, price, description } = product;

      if (!name || !shopId || !sku || !price || !description) {
        return res.status(400).json({ message: FAIL });
      }

      const shopExists = await Shop.exists({ _id: shopId, userProfile: user });

      if (!shopExists) {
        return res.status(404).json({ message: FAIL });
      }

      await Product.create({ name, shop: shopId, sku, price, description });
    }

    return res.status(200).json({ message: SUCCESS });
  } catch (error) {
    console.error(error);
    return res.status(500).json({ message: FAIL });
  }
};

exports.updateProduct = async (req, res) => {
  const user = get_user_for_request(req);

  const { pk } = req.params;
  const data = req.body;

  try {
    const product = await Product.findOne({ _id: pk, 'shop.userProfile': user });

    if (!product) {
      return res.status(404).json({ message: FAIL });
    }

    if (data[NAME]) {
      product.name = data[NAME];
    }
    if (data[SKU]) {
      product.sku = data[SKU];
    }
    if (data[PRICE]) {
      product.price = data[PRICE];
    }
    if (data[DESCRIPTION]) {
      product.description = data[DESCRIPTION];
    }
    if (data[DISCOUNT]) {
      product.discount = data[DISCOUNT];
    }
    if (data[UNIT_IN_STOCK]) {
      product.unitsInStock = data[UNIT_IN_STOCK];
    }
    if (data[SIZE]) {
      product.size = data[SIZE];
    }
    if (data[COLOUR]) {
      product.colour = data[COLOUR];
    }
    if (data[UNIT_WEIGHT]) {
      product.unitWeight = data[UNIT_WEIGHT];
    }

    await product.save();

    return res.status(200).json({ message: SUCCESS });
  } catch (error) {
    console.error(error);
    return res.status(500).json({ message: FAIL });
  }
};

exports.deleteProducts = async (req, res) => {
  const user = get_user_for_request(req);

  const { ids } = req.body;

  if (!ids) {
    return res.status(400).json({ message: FAIL });
  }

  try {
    const products = await Product.find({ _id: { $in: ids }, 'shop.userProfile': user });

    if (products.length !== ids.length) {
      return res.status(404).json({ message: FAIL });
    }

    for (const product of products) {
      await product.delete();
    }

    return res.status(200).json({ message: SUCCESS });
  } catch (error) {
    console.error(error);
    return res.status(500).json({ message: FAIL });
  }
};
