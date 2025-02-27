// shared.js
let socket;

function connectWebSocket(userEmail) {
    if (socket && socket.readyState === WebSocket.OPEN) {
        console.log("WebSocket already connected.");
        return;
    }
    if (!socket || socket.readyState === WebSocket.CLOSED) {
        socket = new WebSocket(`ws://127.0.0.1:8000/ws/notifications/${userEmail}/`);
    }

    //socket = new WebSocket(`ws://127.0.0.1:8000/ws/notifications/${userEmail}/`);

    socket.onopen = () => {
        console.log("WebSocket connected.");
        
    };

    socket.onclose = () => {
        console.log("WebSocket disconnected.");
        setTimeout(() => connectWebSocket(userEmail), 3000); // Reconnect
    };

    socket.onerror = (error) => {
        console.error("WebSocket error:", error);
    };

    socket.onmessage = (event) => {
        console.log("in onmessage");
        try {
            const data = JSON.parse(event.data);
            if (data.type === "error") {
                console.error("Error from server:", data.message);
                return;
            }
            if (data.type === "notification") {
                displayNotification(data); // Call a display function (defined on each page)
            }
        } catch (error) {
            console.error("Error parsing message:", error);
        }
    };



}
function sendMessage(receiverEmail, message, type) {
    console.log("sendmessage");
    if (socket && socket.readyState === WebSocket.OPEN) {
        console.log("in if");
        socket.send(JSON.stringify({receiver_email: receiverEmail, message, type }));
    } else {
        console.error("WebSocket is not connected. Call connectWebSocket first.");
    }
}