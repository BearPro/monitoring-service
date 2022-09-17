package main

import (
	"crypto/sha256"
	"database/sql"
	"encoding/base64"
	"log"
	"os"

	"github.com/gin-gonic/gin"
	_ "github.com/lib/pq"
)

func main() {
	router := gin.Default()
	router.POST("/statusAlive", statusAlive)
	router.Run("localhost:8080")
}

type Message struct {
	Text     string `json:"text"`
	Hostname string `json:"hostname"`
}

func getConnection() *sql.DB {
	connectionString := os.Getenv("RECEIVER_CONNSTR")
	db, err := sql.Open("postgres", connectionString)
	if err != nil {
		panic(err)
	}
	if err := db.Ping(); err != nil {
		panic(err)
	}
	return db
}

func statusAlive(c *gin.Context) {
	db := getConnection()
	token_hash := getTokenHash(c)
	token_found := checkToken(db, token_hash)
	if !token_found {
		c.Status(401)
		return
	}

	var message Message
	if err := c.BindJSON(&message); err != nil {
		c.Status(400)
		return
	}

	// push message to Rabbit
	log.Default().Print(message)
	c.Status(200)

}

func checkToken(db *sql.DB, token_hash string) bool {
	var token_found bool
	rows, err := db.Query("select count(*) > 0 from tokens where value_hash = $1", token_hash)
	if err != nil {
		log.Default().Panic(err)
	}

	rows.Scan(token_found)
	return token_found
}

func getTokenHash(c *gin.Context) string {
	token := c.Request.Header["Token"][0]
	hasher := sha256.New()
	hasher.Write([]byte(token))
	token_hash := base64.StdEncoding.EncodeToString(hasher.Sum(nil))
	return token_hash
}
