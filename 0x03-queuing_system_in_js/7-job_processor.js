const kue = require("kue")

const queue = kue.createQueue();

const blacklistedPhoneNumbers = ['4153518780', '4153518781'];

export default function sendNotification(phoneNumber, message, job, done) {
    job.progress(0, 100)

    if (blacklistedPhoneNumbers.includes(phoneNumber)) {
        const error = new Error(`Phone number ${phoneNumber} is blacklisted`)
        return done(error)
    }
    job.progress(50, 100)
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
}

queue.process('push_notification_code_2', 2, (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message, job, done);
});