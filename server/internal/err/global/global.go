// Package errgl
package errgl

import "errors"

type ErrMessage struct {
	Message string `binding:"required"`
	Type    string `binding:"required"`
}

func (e *ErrMessage) Error() string {
	return e.Message
}

func NewErrMessage(msg string, t string) *ErrMessage {
	return &ErrMessage{
		Message: msg,
		Type:    t,
	}
}

var ErrNotAuthorized = errors.New("not authorized")
