using Confluent.Kafka;
using DotNetWeatherData.Database;


namespace DotNetWeatherData;

static class Program
{
    private static void Main()
    {
        DotEnv.Load(".env");
        var config = new ConsumerConfig
        {
            BootstrapServers = "127.0.0.1:29092,127.0.0.1:29093",
            AutoOffsetReset = AutoOffsetReset.Earliest,
            GroupId = "Open Meteo Service"
        };
        Db database = new Db(
            "localhost",
            "5432",
            "change_me",
            "change_me",
            "weather"
        );
        var subscriber = new KafkaReader(config, ref database);
        subscriber.Run();
    }
}