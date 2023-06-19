// Trigger set on executing once in an hour

exports = async function() {
  const currentDate = new Date();
  const collectionRooms = context.services.get("HotelsCluster").db("HotelsDB").collection("Rooms");
  const collectionBookingLogs = context.services.get("HotelsCluster").db("HotelsDB").collection("Booking_Logs");

  try {
    const filter = { "bookings.date_to": { $lt: currentDate } };
    const projection = { bookings: { $elemMatch: { date_to: { $lt: currentDate } } } };
    const bookingsToRemove = await collectionRooms.find(filter, projection).toArray();

    if (bookingsToRemove.length > 0) {
      const bulkOps = bookingsToRemove.map(booking => ({
        updateOne: {
          filter: { _id: booking._id },
          update: { $pull: { bookings: { date_to: { $lt: currentDate } } } }
        }
      }));

      await collectionRooms.bulkWrite(bulkOps);

      const bookingLogs = bookingsToRemove.flatMap(booking => booking.bookings.map(bookingData => ({
        room_id: booking._id,
        booking_id: bookingData.booking_id,
        customer_id: bookingData.customer_id,
        date_from: bookingData.date_from,
        date_to: bookingData.date_to
      })));

      await collectionBookingLogs.insertMany(bookingLogs);

      console.log(`Moved ${bookingsToRemove.length} bookings to BookingLogs collection.`);
    } else {
      console.log("No bookings to move.");
    }
  } catch (err) {
    console.error(err);
  }
};
