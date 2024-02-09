const kue = require("kue")

const queue = kue.createQueue();

const blacklistedPhoneNumbers = ['4153518780', '4153518781'];

export default function sendNotification(phoneNumber, message, job, done) {

}