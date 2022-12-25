using System.Text.Json;
using Confluent.Kafka;

using DotNetWeatherData.WeatherData;
using DotNetWeatherData.WeatherData.OpenWeather;
using DotNetWeatherData.Database;

namespace DotNetWeatherData;

public class KafkaReader
{
    private ConsumerConfig Config { get; set; }
    private Db Database { get; set; }
    public KafkaReader(ConsumerConfig config, ref Db database)
    {
        Config = config;
        Database = database;
    }
    
    public void Run()
    {
        CancellationTokenSource cancellationToken = new();
        var consumer = new ConsumerBuilder<string, string>(Config);
        using var consumerBuild = consumer.Build();
        consumerBuild.Subscribe("Weather");
        int i = 0;
        while(i < 100)
        {
            var message = consumerBuild.Consume(cancellationToken.Token);
                
            if (message.Message is { Key: "Open Meteo Service" })
            {
                var deserialized = JsonSerializer.Deserialize<DataService<OpenWeatherData>>(message.Message.Value);
                if (deserialized is not null)
                {
                    Database.LoadWeatherToDb(deserialized);
                }
            }
            i++;
        }
    }
}