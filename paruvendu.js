const { Client } = require('pg');
const express = require('express');
const app = express();
const cors = require('cors')
app.use(cors());


const client = new Client({
  host: "localhost",
  user: "postgres",
  password: "12365478901",
  database: "paruvendu",
  port: 5432,
});

app.use(express.json());

app.get('/', (req, res) => {
    res.send("Salut");
});

app.get('/api/all', async (req, res) => {
    try {
        const data = await retrieveAll();
        res.json(data);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

app.listen(9000, async () => {
    await client.connect();
    console.log("✅ Connecté à PostgreSQL");
    console.log("🚀 Serveur démarré sur http://localhost:9000/");
});

async function retrieveAll() {
    const result = await client.query("SELECT * FROM biens;");
    return result.rows;
}
