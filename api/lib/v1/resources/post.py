from flask import request, abort
from ..extraResource import ExtraResource


class NewPost(ExtraResource):
    def post(self):
        return str(request.get_json())


class CreatedPost(ExtraResource):
    def get(self, postID, userID=None):
        returnString = ""
        if userID is not None:
            returnString += "From user {}, g".format(userID)
        else:
            returnString += "G"
        returnString += "et post number {1}!".format(userID, postID)
        return returnString

    def update(self, postID, userID=None):
        return "From user {0}, update post number {1}!".format(userID, postID)

    def delete(self, postID, userID=None):
        returnString = ""
        if userID is not None:
            returnString += "From user {}, d".format(userID)
        else:
            returnString += "D"

        returnString += "elete post number {0}!".format(postID)
        return returnString
