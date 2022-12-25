namespace DotNetWeatherData.WeatherData;

public class BaseWeatherData
{
    private Dictionary<string, string> Mapper;
    public Guid Id { get; set; }

    public virtual void SetDictionary(Dictionary<string, string> NewMapper)
    {
        Mapper = NewMapper;
    }

    public Dictionary<string, string> GetMapper()
    {
        return Mapper;
    }
}