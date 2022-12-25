namespace DotNetWeatherData.WeatherData;

public abstract class BaseWeatherData
{
    public abstract Dictionary<string, string?> GetMapper();

    public abstract Dictionary<string, string?> ToDictionary();

    public abstract string GetServiceTableName();
}