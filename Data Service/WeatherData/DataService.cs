using System.Globalization;

namespace DotNetWeatherData.WeatherData;

public class DataService<T> where T: BaseWeatherData
{
    public string? Place { get; set; }
    public T[] Data { get; set; }
    public DateTime Created { get; set; }

    public Dictionary<string, string?> ToDictionary(T dataRow)
    {
        if (Place is not null)
        {
            var result = dataRow.ToDictionary();
            result.Add("Place", Place);
            result.Add("Created", Created.ToString(CultureInfo.InvariantCulture));
            return result;
        }
        throw new Exception("No place was provided");
    }

    public Dictionary<string, string?> GetMapper()
    {
        if (Data is { Length: > 0 } && Place is not null)
        {
            var mapper = Data[0].GetMapper();
            mapper.Add("Place", "place");
            mapper.Add("Created", "created");
            return mapper;
        }
        throw new Exception("No data was provided");
    }

    public string GetTableName()
    {
        if (Data is { Length: > 0 } && Place is not null)
        {
            return Data[0].GetServiceTableName();
        }

        throw new Exception("No table name was provided!");
    }
}