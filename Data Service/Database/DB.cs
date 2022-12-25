using DotNetWeatherData.WeatherData;
using Npgsql;

namespace DotNetWeatherData.Database;

public class Db
{
    private readonly string _connectionString;
    private readonly NpgsqlDataSource _dataSource;
    public Db()
    {
        string? host = Environment.GetEnvironmentVariable("DATABASE_HOST");
        string? port = Environment.GetEnvironmentVariable("DATABASE_PORT");
        string? user = Environment.GetEnvironmentVariable("DATABASE_USER");
        string? password = Environment.GetEnvironmentVariable("DATABASE_PASSWORD");
        string? database = Environment.GetEnvironmentVariable("DATABASE_DB");
        if (host == null || port == null || user == null || password == null || database == null)
        {
            throw new ArgumentException("Some connection data is not in environment");
        }
        _connectionString = $"Host={host};Port={port};Username={user};Password={password};Database={database}";
        _dataSource = InitConnection();
    }

    public Db(string host, string port, string user, string password, string database)
    {
        _connectionString = $"Host={host};Port={port};Username={user};Password={password};Database={database};" +
                            $"Pooling=true;Minimum Pool Size=0;Maximum Pool Size=100;";
        _dataSource = InitConnection();
    }

    private NpgsqlDataSource InitConnection()
    {
        try
        {
            return new NpgsqlDataSourceBuilder(_connectionString).Build();
        }
        catch (Exception e)
        {
            Console.WriteLine(e);
            throw;
        }
    
    }
    
    public async void LoadWeatherToDb<T>(DataService<T> dataService) where T: BaseWeatherData
    {
        await using NpgsqlConnection connection = await _dataSource.OpenConnectionAsync();
        if (dataService.Data.Length <= 0) return;
        var mapper = dataService.GetMapper();
        string propertyString = "";
        foreach (var property in mapper.Keys)
        {
            propertyString += mapper[property] + ", ";

        }
        propertyString = propertyString.Remove(propertyString.Length - 2);
        
        string values = "";
        foreach (var dataRow in dataService.Data)
        {
            var rowDict = dataService.ToDictionary(dataRow);
            string rowValue = "(";
            foreach (var property in mapper.Keys)
            {
                rowValue += "'" + rowDict[property] + "'" + ",";
            }

            rowValue = rowValue.Remove(rowValue.Length - 1);
            rowValue += ")";
            values += rowValue + ", ";
        }

        values = values.Remove(values.Length - 2);
        
        string sql = $"INSERT INTO weather.{dataService.GetTableName()} ({propertyString}) VALUES {values}";

        await using var command = new NpgsqlCommand(
            sql,
            connection
        );
        await command.ExecuteNonQueryAsync();

    }
}