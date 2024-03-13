db.createCollection('users');

db.createUser(
        {
            user: "admin",
            pwd: "admin",
            roles: ["readWrite"]
        }
);
