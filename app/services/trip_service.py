from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from datetime import time
from app.schemas.trips import TripSchema

def get_trips_from_alicante(db: Session, date: str):
    """
    Obtiene los viajes que pasan por Alicante en una fecha específica.
    """
    query = text("""
        SELECT 
            t.trip_id, 
            t.service_id,
            (SELECT s.stop_name 
             FROM stops s
             JOIN stop_times st ON s.stop_id = st.stop_id
             WHERE st.trip_id = t.trip_id 
               AND s.stop_name LIKE '%Alicante/alacant%'
             ORDER BY st.stop_sequence ASC
             LIMIT 1) AS first_stop_name,
             
            (SELECT st.stop_sequence
             FROM stop_times st
             JOIN stops s ON s.stop_id = st.stop_id
             WHERE st.trip_id = t.trip_id 
               AND s.stop_name LIKE '%Alicante/alacant%'
             ORDER BY st.stop_sequence ASC
             LIMIT 1) AS first_stop_sequence,
             
            (SELECT st.arrival_time 
             FROM stop_times st
             JOIN stops s ON s.stop_id = st.stop_id
             WHERE st.trip_id = t.trip_id 
               AND s.stop_name LIKE '%Alicante/alacant%'
             ORDER BY st.stop_sequence ASC
             LIMIT 1) AS first_arrival_time,
             
            (SELECT st.departure_time 
             FROM stop_times st
             JOIN stops s ON s.stop_id = st.stop_id
             WHERE st.trip_id = t.trip_id 
               AND s.stop_name LIKE '%Alicante/alacant%'
             ORDER BY st.stop_sequence ASC
             LIMIT 1) AS first_departure_time,
             
            (SELECT s.stop_name 
             FROM stops s
             JOIN stop_times st ON s.stop_id = st.stop_id
             WHERE st.trip_id = t.trip_id 
               AND s.stop_name NOT LIKE '%Alicante/alacant%'
               AND st.stop_sequence > 
                   (SELECT MIN(stop_sequence) 
                    FROM stop_times 
                    JOIN stops ON stops.stop_id = stop_times.stop_id 
                    WHERE trip_id = t.trip_id 
                      AND stop_name LIKE '%Alicante/alacant%')
             ORDER BY st.stop_sequence DESC
             LIMIT 1) AS last_stop_name,

            (SELECT st.stop_sequence
             FROM stop_times st
             JOIN stops s ON s.stop_id = st.stop_id
             WHERE st.trip_id = t.trip_id 
               AND s.stop_name NOT LIKE '%Alicante/alacant%'
               AND st.stop_sequence > 
                   (SELECT MIN(stop_sequence) 
                    FROM stop_times 
                    JOIN stops ON stops.stop_id = stop_times.stop_id 
                    WHERE trip_id = t.trip_id 
                      AND stop_name LIKE '%Alicante/alacant%')
             ORDER BY st.stop_sequence DESC
             LIMIT 1) AS last_stop_sequence,

            (SELECT st.arrival_time 
             FROM stop_times st
             JOIN stops s ON s.stop_id = st.stop_id
             WHERE st.trip_id = t.trip_id 
               AND s.stop_name NOT LIKE '%Alicante/alacant%'
               AND st.stop_sequence > 
                   (SELECT MIN(stop_sequence) 
                    FROM stop_times 
                    JOIN stops ON stops.stop_id = stop_times.stop_id 
                    WHERE trip_id = t.trip_id 
                      AND stop_name LIKE '%Alicante/alacant%')
             ORDER BY st.stop_sequence DESC
             LIMIT 1) AS last_arrival_time,

            (SELECT st.departure_time 
             FROM stop_times st
             JOIN stops s ON s.stop_id = st.stop_id
             WHERE st.trip_id = t.trip_id 
               AND s.stop_name NOT LIKE '%Alicante/alacant%'
               AND st.stop_sequence > 
                   (SELECT MIN(stop_sequence) 
                    FROM stop_times 
                    JOIN stops ON stops.stop_id = stop_times.stop_id 
                    WHERE trip_id = t.trip_id 
                      AND stop_name LIKE '%Alicante/alacant%')
             ORDER BY st.stop_sequence DESC
             LIMIT 1) AS last_departure_time,

            r.route_short_name

        FROM trips t
        JOIN routes r ON t.route_id = r.route_id  
        JOIN calendar c ON t.service_id = c.service_id 

        WHERE t.trip_id IN (
            SELECT DISTINCT trip_id 
            FROM stop_times st 
            JOIN stops s ON s.stop_id = st.stop_id 
            WHERE s.stop_name LIKE '%Alicante/alacant%'
        )
        AND (
            :date BETWEEN c.start_date AND c.end_date
            AND (
                (c.monday = '1' and EXTRACT(DOW FROM DATE :date) = 1) OR
                (c.tuesday = '1' and EXTRACT(DOW FROM DATE :date) = 2) OR
                (c.wednesday = '1' and EXTRACT(DOW FROM DATE :date) = 3) OR
                (c.thursday = '1' and EXTRACT(DOW FROM DATE :date) = 4) OR
                (c.friday = '1' and EXTRACT(DOW FROM DATE :date) = 5) OR
                (c.saturday = '1' and EXTRACT(DOW FROM DATE :date) = 6) OR
                (c.sunday = '1' and EXTRACT(DOW FROM DATE :date) = 0)
            )
        )
        AND t.service_id NOT IN (
            SELECT service_id FROM calendar_date WHERE date = :date AND exception_type = 2
        )
        AND t.trip_id NOT IN (
            SELECT trip_id
            FROM stop_times st
            JOIN stops s ON s.stop_id = st.stop_id
            WHERE s.stop_name LIKE '%Alicante/alacant%'
            AND st.stop_sequence = (SELECT MAX(stop_sequence) FROM stop_times WHERE trip_id = st.trip_id)
        )
        ORDER BY first_arrival_time;
    """)

    result = db.execute(query, {"date": date}).fetchall()
    return [
    TripSchema(
        **{
            key: (value.strftime("%H:%M") if isinstance(value, time) else value)
            for key, value in row._asdict().items()
        }
    )
    for row in result
    ]
