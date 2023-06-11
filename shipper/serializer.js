const { Schema, model } = require('mongoose');

const shipperSchema = new Schema({
  type: { type: Number, required: true },
  companyName: { type: String, required: true },
  trackingUrl: { type: String, unique: true },
  urlStatus: { type: Number },
  checkPoints: { type: Array },
  totalCheckPoints: { type: Number },
  currentCheckPoint: { type: Number },
});

const Shipper = model('Shipper', shipperSchema);

class ShipperSerializer {
  static toResponse(shipper) {
    const { _id, ...data } = shipper.toObject();
    data.id = _id.toString();
    return data;
  }

  static fromRequest(payload) {
    return new Shipper(payload);
  }
}

module.exports = { Shipper, ShipperSerializer };
