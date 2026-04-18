// Package health
package health

import (
	"github.com/gin-gonic/gin"
	"net/http"
	"server/internal/db/pg"
	"server/internal/db/red"
)

func Health(c *gin.Context) {
	// Postgres health check
	if err := pg.DB.Ping(); err != nil {
		c.JSON(http.StatusInternalServerError, map[string]string{
			"message": "PostgreSql Database failed to init: " + err.Error(),
		})
		panic("Failed to init db")
	}
	// Redis health check
	if err := red.Client.Ping(red.Ctx).Err(); err != nil {
		c.JSON(http.StatusInternalServerError, map[string]string{
			"message": "Redis failed to init: " + err.Error(),
		})
		panic("Failed to init db")
	}
	// Success
	c.JSON(http.StatusOK, map[string]string{
		"message": "Success",
	})
}
