using System.Text.Json;
using Confluent.Kafka;
using DotNetWeatherData.WeatherData;
using DotNetWeatherData.WeatherData.OpenWeather;

namespace DotNetWeatherData;

class Program
{
    static void Main()
    {
        DotEnv.Load(".env");
        var config = new ConsumerConfig
        {
            BootstrapServers = "127.0.0.1:29092,127.0.0.1:29093",
            AutoOffsetReset = AutoOffsetReset.Earliest,
            GroupId = "Open Meteo Service"
        };

        CancellationTokenSource cancellationToken = new();
        var consumer = new ConsumerBuilder<string, string>(config);
        using (var consumerBuild = consumer.Build())
        {
            consumerBuild.Subscribe("Weather");
            int i = 0;
            while(i < 100)
            {
                var message = consumerBuild.Consume(cancellationToken.Token);
                
                if (message.Message != null)
                {
                    if (message.Message.Key == "Open Meteo Service")
                    {
                        var deserialized = JsonSerializer.Deserialize<DataService<OpenWeatherData>>(message.Message.Value);
                        if (deserialized != null)
                        {
                            Console.WriteLine($"Weather in {deserialized.Place} with first id {deserialized.Data[0].Id}");
                        }
                        else
                        {
                            Console.WriteLine("Wrong data!");
                        }
                    }

                }
                i++;
            }
        }
    }
}