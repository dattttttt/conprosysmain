// db/init/init.js

db = db.getSiblingDB("omron");
db.createCollection("sensor");
db.sensor.insertMany([
    {
        UUID: "test-uuid",
        T: "2025-05-16T15:30:00.000+09:00",
        SN: "TEST123",
        CK: "send",
        DATA: [
            { ID: "TAG100", NE: "temperature", V: 28.5 },
            { ID: "TAG101", NE: "Humidity", V: 55.5 }
        ],
        timestamp: "2025-05-16 06:30:00"
    }
]);
