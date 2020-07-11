from spotify_credentials import USERNAME, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
from spotipy import util
from list_of_scopes import list_of_scopes

class Token:
    @classmethod
    def get_token(cls) -> str:
        return util.prompt_for_user_token(USERNAME, 
            cls.get_scopes_str(),
            CLIENT_ID,
            CLIENT_SECRET,
            REDIRECT_URI)
    
    @classmethod
    def get_scopes_str(cls) -> str:
        scopes_to_generate_token_for = ''
        for scope in list_of_scopes:
            scopes_to_generate_token_for += '{0}%20'.format(scope)
        return scopes_to_generate_token_for