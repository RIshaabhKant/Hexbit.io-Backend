const express = require('express');
const router = express.Router();
const { check, validationResult } = require('express-validator');

const Shop = require('../models/shop');

const SUCCESS = 'Success';
const FAIL = 'Fail';

// API Functions

// Initialize the shop section for a user
router.post('/initialize', [
  check('userProfile_id').notEmpty().withMessage('User profile ID is required'),
  check('name').notEmpty().withMessage('Name is required'),
], async (req, res) => {
  try {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ message: FAIL, errors: errors.array() });
    }

    const userProfileId = req.body.userProfile_id;
    const name = req.body.name;
    const city = req.body.city || '';
    const state = req.body.state || '';
    const accountNumber = req.body.accountNumber || '';
    const ifscCode = req.body.ifscCode || '';
    const incorporationName = req.body.incorporationName || '';
    const incorporationType = req.body.incorporationType || '';
    const gstin = req.body.gstin || '';
    const pan = req.body.pan || '';
    const phone = req.body.phone || '';
    const email = req.body.email || '';

    const shop = new Shop({
      userProfile: userProfileId,
      name: name,
      city: city,
      state: state,
      accountNumber: accountNumber,
      ifscCode: ifscCode,
      incorporatioName: incorporationName,
      incorporationType: incorporationType,
      gstin: gstin,
      pan: pan,
      phone: phone,
      email: email,
    });

    await shop.save();

    return res.status(200).json({ message: SUCCESS, shop: shop.name });
  } catch (error) {
    console.error(error);
    return res.status(500).json({ message: FAIL });
  }
});

module.exports = router;
