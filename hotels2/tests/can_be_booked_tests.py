from bson.objectid import ObjectId
from datetime import datetime
from hotels2.server.dbOperations import can_be_booked


if __name__ == '__main__':
    customer_id = ObjectId('648ec52ebf5b866d9e06c621')
    booking_id = ObjectId('648f80ec7e8828488627815a')
    different_customer_id = ObjectId('648c30c240567fa6e3d1177f')
    room_id = ObjectId('648b44e51905fb3623930783')
    check_in = datetime(2023, 9, 15)
    check_out = datetime(2023, 9, 20)
    left_1 = datetime(2023, 9, 1)
    left_2 = datetime(2023, 9, 10)
    inside_1 = datetime(2023, 9, 16)
    inside_2 = datetime(2023, 9, 18)
    right_1 = datetime(2023, 9, 22)
    right_2 = datetime(2023, 9, 30)

    assert can_be_booked(room_id, left_1, left_2)
    assert can_be_booked(room_id, left_1, check_in)
    assert can_be_booked(room_id, check_out, right_2)
    assert can_be_booked(room_id, right_1, right_2)

    assert not can_be_booked(room_id, inside_1, inside_2)
    assert can_be_booked(room_id, inside_1, inside_2, booking_id)

    assert not can_be_booked(room_id, left_1, inside_1)
    assert can_be_booked(room_id, left_1, inside_1, booking_id)

    assert not can_be_booked(room_id, check_in, inside_1)
    assert can_be_booked(room_id, check_in, inside_1, booking_id)

    assert not can_be_booked(room_id, left_1, check_out)
    assert can_be_booked(room_id, left_1, check_out, booking_id)

    assert not can_be_booked(room_id, check_in, right_1)
    assert can_be_booked(room_id, check_in, right_1, booking_id)

    assert not can_be_booked(room_id, left_1, right_1)
    assert can_be_booked(room_id, left_1, right_1, booking_id)

    assert not can_be_booked(room_id, check_in, check_out)
    assert can_be_booked(room_id, check_in, check_out, booking_id)

    assert not can_be_booked(room_id, inside_1, check_out)
    assert can_be_booked(room_id, inside_1, check_out, booking_id)

    assert not can_be_booked(room_id, inside_1, right_2)
    assert can_be_booked(room_id, inside_1, right_2, booking_id)