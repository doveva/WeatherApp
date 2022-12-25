using System.Globalization;

namespace DotNetWeatherData.WeatherData.OpenWeather;

public class OpenWeatherData: BaseWeatherData
{
    public Guid Id { get; set; }
    public float Dewpoint { get; set; }
    public string? Weather { get; set; }
    public int CloudCover { get; set; }
    public float WindSpeedLow { get; set; }
    public int? WindDirectionLow { get; set; }
    public float WindSpeedHigh { get; set; }
    public int? WindDirectionHigh { get; set; }
    public DateTime Datetime { get; set; }

    private Dictionary<string, string?> BaseMapper = new Dictionary<string, string?>()
        {
            {"Id", "id"},
            {"Dewpoint", "dewpoint"},
            {"Weather", "weather"},
            {"CloudCover", "cloud_cover"},
            {"WindSpeedLow", "wind_speed_low"},
            {"WindDirectionLow", "wind_direction_low"},
            {"WindSpeedHigh", "wind_speed_high"},
            {"WindDirectionHigh", "wind_direction_high"},
            {"Datetime", "date"}
        };

    public override Dictionary<string, string?> ToDictionary()
    {
        return new Dictionary<string, string?>()
        {
            {"Id", Id.ToString()},
            {"Dewpoint", Dewpoint.ToString(CultureInfo.InvariantCulture)},
            {"Weather", Weather},
            {"CloudCover", CloudCover.ToString()},
            {"WindSpeedLow", WindSpeedLow.ToString(CultureInfo.InvariantCulture)},
            {"WindDirectionLow", WindDirectionLow.ToString()},
            {"WindSpeedHigh", WindSpeedHigh.ToString(CultureInfo.InvariantCulture)},
            {"WindDirectionHigh", WindDirectionHigh.ToString()},
            {"Datetime", Datetime.ToString(CultureInfo.InvariantCulture)}
        };
    }

    public override Dictionary<string, string?> GetMapper()
    {
        return BaseMapper;
    }

    public override string GetServiceTableName()
    {
        return "openweather";
    }
}