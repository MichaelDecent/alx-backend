const kue = require("kue")

const queue = kue.createQueue();

const jobData = {
    phoneNumber: '+2348012345678',
    message: 'Your order has been shipped!',
};
  
const job = queue.create('push_notification_code', jobData).save(function(error) {
    if (!error) {
        console.log('Notification job created:', job.id);
    } else {
        console.error("Notification job failed");
    }
})

job.on('job completed', () => {
    console.log("Notification job completed")
})

