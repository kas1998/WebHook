const express = require("express");
const bodyParser = require("body-parser");

const app = express();
const PORT = 5000;

// Middleware para parsear JSON
app.use(bodyParser.json());
app.use(express.static("public"));

// Ruta para el Webhook
app.post("/webhook", (req, res) => {
    console.log("Evento recibido:");
    console.log(req.body);

    // Responder al emisor del Webhook
    res.status(200).json({ message: "Evento recibido" });
});

// Iniciar el servidor
app.listen(PORT, () => {
    console.log(`Servidor en http://localhost:${PORT}`);
});