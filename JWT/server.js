const express = require("express");
const jwt = require("jsonwebtoken");
const bodyParser = require("body-parser");
const path = require("path");

const app = express();
const PORT = 3000;
const SECRET_KEY = "supersecretkey";

app.use(bodyParser.json());
app.use(express.static("public"));


const users = { 
    admin: "darthvarder",
    user: "password123"
};


app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "public", "jwt.html"));
});


app.post("/login", (req, res) => {
    const { username, password } = req.body;
    if (users[username] && users[username] === password) {
        const token = jwt.sign({ username, role: "user" }, SECRET_KEY);
        return res.json({ token });
    }
    return res.status(401).json({ error: "Invalid credentials" });
});


app.get("/flag", (req, res) => {
    const token = req.headers.authorization;
    if (!token) return res.status(403).json({ error: "No token provided" });
    
    try {
        const decoded = jwt.decode(token); 
        if (decoded.role === "admin") {
            return res.json({ flag: "KALAM25{jw7_9wn3d}" });
        }
        return res.status(403).json({ error: "Not an admin" });
    } catch (err) {
        return res.status(400).json({ error: "Invalid token" });
    }
});

app.listen(PORT, () => {
    console.log(`CTF server running on http://localhost:${PORT}`);
});
