using DotNetWeatherData.WeatherData;

namespace DotNetWeatherData.Database;

public class Db
{
    private string connectionString;
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
        connectionString = $"Host={host};Port={port};Username={user};Password={password};Database={database}";
    }

    public Db(string host, string port, string user, string password, string database)
    {
        connectionString = $"Host={host};Port={port};Username={user};Password={password};Database={database}";
    }

    public void LoadDb<T>(DataService<T> dataService) where T: BaseWeatherData
    {
        
    }
    
}