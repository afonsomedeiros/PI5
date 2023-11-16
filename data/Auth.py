from jwt_bottle import BaseAuth
from data.database import get_user, get_user_email, verify

class Auth(BaseAuth):
    """Classe para autenticação.
    Precisa conter um método estático chamado authenticate e outro
    chamado get_user. Também deve herdar de jwt_bottle.BaseAuth.

    Os parametros de authenticate ficam a critério do método post.

    O padrão é receber uma requisição POST enviando dados no formato JSON.
    Esses dados são empacotados no argumento kwargs do método authenticate.

    para identificar o usuário é necessário realizar a consulta utilizando
    um ID.
    """

    @staticmethod
    def authenticate(*args, **kwargs):
        """Método para autenticação, aqui utilizei uma classe chamada
        Users implementada com o ORM peewee e uma simples regra de 
        autenticação apresentada pelo Eduardo Mendes.
        link: https://www.youtube.com/watch?v=ieGA91ExOH0

        Returns:
            Users: dicionário contendo id para gerar o token.
            OBS: é necessário possuir um atributo "id" para gerar o token.
        """
        try:
            if "email" in kwargs and "password" in kwargs:
                user = get_user_email(kwargs['email'])
                password = kwargs['password']
                secret = ""
                if verify(password=password, user_password=user['password'], secret=secret):
                    return user
            return None
        except Exception as err:
            return {"erro": f"Usuário {kwargs['email']} não localizado"}

    @staticmethod
    def get_user(*args, **kwargs):
        """Classe para resgatar usuario autenticado
        utilizando a decodificação de um token.

        Args:
            user_id ([int]): identificador do usuário.

        Returns:
            Users: retorna usuário autenticado pelo Token.
        """
        try:
            user = get_user(kwargs["_id"])
            if user:
                return user
            return None
        except Exception as err:
            return {}
        

