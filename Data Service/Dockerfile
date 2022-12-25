FROM mcr.microsoft.com/dotnet/runtime:6.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /src
COPY ["DotNetWeatherData.csproj", "./"]
RUN dotnet restore "DotNetWeatherData.csproj"
COPY . .
WORKDIR "/src/"
RUN dotnet build "DotNetWeatherData.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "DotNetWeatherData.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "DotNetWeatherData.dll"]
