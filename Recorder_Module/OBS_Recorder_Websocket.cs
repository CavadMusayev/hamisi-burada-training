using System;
using System.Net.WebSockets;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using netcore.template;

namespace Recorder_Module
{
    public class OBSSocket
    {
        private static ClientWebSocket _webSocket;
        public static async Task OpenConnection()
        {
            _webSocket = new();
            Uri serverUri = new($"ws://localhost:{CONSTANTlar.OBS_SOCKET_PORT}");
            CancellationTokenSource cts = new(TimeSpan.FromSeconds(10)); // Set timeout to 10 seconds
            await _webSocket.ConnectAsync(serverUri, cts.Token);
        }

        public static async Task StartRecording()
        {
            string startRecordingMessage = "{\"request-type\": \"StartRecording\", \"message-id\": \"1\"}";
            await SendMessage(startRecordingMessage);
            Console.WriteLine("Sent StartRecording request to OBS");
            Console.WriteLine(await ReceiveMessage());
        }

        public static async Task StopRecording()
        {
            string stopRecordingMessage = "{\"request-type\": \"StopRecording\", \"message-id\": \"2\"}";
            await SendMessage(stopRecordingMessage);
            Console.WriteLine("Sent StopRecording request to OBS");
            Console.WriteLine(await ReceiveMessage());
        }

        
        public static async Task CloseConnection()
        {
            await _webSocket.CloseAsync(WebSocketCloseStatus.NormalClosure, "Closing", CancellationToken.None);
        }

        private static async Task SendMessage(string message)
        {
            byte[] messageBuffer = Encoding.UTF8.GetBytes(message);
            await _webSocket.SendAsync(new ArraySegment<byte>(messageBuffer), WebSocketMessageType.Text, true, CancellationToken.None);
        }

        private static async Task<string> ReceiveMessage()
        {
            byte[] buffer = new byte[1024];
            var result = await _webSocket.ReceiveAsync(new ArraySegment<byte>(buffer), CancellationToken.None);
            return Encoding.UTF8.GetString(buffer, 0, result.Count);
        }
    }
}