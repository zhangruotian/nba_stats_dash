from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players
from pandas import DataFrame
from typing import Union
import pandas as pd


class FetchPlayerData:

    def __get_all_players(self) -> list[dict]:
        return players.get_players()

    def __get_player_by_id(self, player_id: Union[str, int]) -> dict:
        return players.find_player_by_id(player_id)

    def __get_player_by_full_name(self, full_name: str) -> Union[dict, None]:
        players_intended = players.find_players_by_full_name(full_name)
        if players_intended:
            return players_intended[0]
        return None

    def __get_career_stats_by_id(self, player_id: Union[str, int]) -> DataFrame:
        return playercareerstats.PlayerCareerStats(player_id).get_data_frames()[0]

    def get_career_stats_by_full_name(self, full_name: str) -> DataFrame:
        player = self.__get_player_by_full_name(full_name)
        if player:
            return self.__get_career_stats_by_id(player.get('id'))
        return DataFrame()


class Player:
    def __init__(self, career_data: DataFrame):
        self.career_data = career_data
        self.__add_more_stats()
        self.stat_names = ('PLAYER_AGE', 'PPG', 'RPG', 'APG', 'FG3_PCT', 'FG_PCT', 'FT_PCT', 'STPG', 'TOVPG')
        self.career_data_updated = self.__all_season_average_stats()

    def __add_more_stats(self) -> None:
        self.career_data['PPG'] = self.career_data['PTS'] / self.career_data['GP']
        self.career_data['RPG'] = self.career_data['REB'] / self.career_data['GP']
        self.career_data['APG'] = self.career_data['AST'] / self.career_data['GP']
        self.career_data['ORPG'] = self.career_data['OREB'] / self.career_data['GP']
        self.career_data['TOVPG'] = self.career_data['TOV'] / self.career_data['GP']
        self.career_data['STPG'] = self.career_data['STL'] / self.career_data['GP']

    def __all_season_average_stats(self):
        all_season_average_stats = []
        for index, one_season in self.career_data.iterrows():
            season_avg = {}
            season_avg['SEASON'] = one_season['SEASON_ID']
            season_avg['TEAM'] = one_season['TEAM_ABBREVIATION']
            for stat_name in self.stat_names:
                season_avg[stat_name] = round(one_season[stat_name], 2)
            all_season_average_stats.append(season_avg)
        return DataFrame(all_season_average_stats)

    def season_average_stats(self, seasons: list[str]) -> DataFrame:
        if 'all' in seasons:
            return self.career_data_updated.copy()
        aggregated_data = []
        for season in seasons:
            season_data = self.career_data_updated[self.career_data_updated['SEASON'] == season]
            aggregated_data.append(season_data)
        return pd.concat(aggregated_data, axis=0)


if __name__ == '__main__':
    fpd = FetchPlayerData()
    career_data = fpd.get_career_stats_by_full_name('Stephen Curry')
    sc = Player(career_data)
    a = sc.season_average_stats(['2016-17', '2017-18'])
    pass
