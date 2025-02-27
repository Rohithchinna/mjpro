// sharedWorker.js
let socket;

self.onconnect = function(event) {
    const port = event.ports[0];

    port.onmessage = function(event) {
        const { userEmail, action, message } = event.data;

        if (action === 'connect') {
            if (!socket || socket.readyState === WebSocket.CLOSED) {
                socket = new WebSocket(`ws://127.0.0.1:8000/ws/notifications/${userEmail}/`);

                socket.onopen = () => {
                    console.log("WebSocket connected.");
                    port.postMessage({ type: 'connected' });
                };

                socket.onclose = () => {
                    console.log("WebSocket disconnected.");
                    setTimeout(() => {
                        port.postMessage({ type: 'reconnect' });
                    }, 3000); // Attempt to reconnect
                };

                socket.onerror = (error) => {
                    console.error("WebSocket error:", error);
                };

                socket.onmessage = (event) => {
                    const data = JSON.parse(event.data);
                    port.postMessage({ type: 'message', data });
                };
            } else {
                port.postMessage({ type: 'connected' });
            }
        } else if (action === 'send') {
            if (socket && socket.readyState === WebSocket.OPEN) {
                socket.send(JSON.stringify(message));
            } else {
                console.error("WebSocket is not connected.");
            }
        }
    };
};