using System;
using Grpc.Core;
using RpcDemo;

namespace RpcDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            Channel channel = new Channel("127.0.0.1:50051", ChannelCredentials.Insecure);

            var client = new CoordsComm.CoordsCommClient(channel);
            while (true){
                var reply = client.getCoords(new RpcDemo.Empty {});
                Console.WriteLine(reply);
            }
            //channel.ShutdownAsync().Wait();
            //Console.WriteLine("Press any key to exit...");
            //Console.ReadKey();
        }
    }
}
