namespace DotNetWeatherData.WeatherData;

public class DataService<T> where T: BaseWeatherData
{
    public string ServiceName { get; set; }
    public string Place { get; set; }
    public T[] Data { get; set; }
    public DateTime Created { get; set; }
}