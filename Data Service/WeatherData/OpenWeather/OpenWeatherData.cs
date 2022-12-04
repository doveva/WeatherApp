namespace DotNetWeatherData.WeatherData.OpenWeather;

public class OpenWeatherData: BaseWeatherData
{
    
    public float Dewpoint { get; set; }
    public string? Weather { get; set; }
    public int CloudCover { get; set; }
    public float WindSpeedLow { get; set; }
    public int? WindDirectionLow { get; set; }
    public float? WindSpeedHigh { get; set; }
    public int? WindDirectionHigh { get; set; }
    public DateTime DateTime { get; set; }
}