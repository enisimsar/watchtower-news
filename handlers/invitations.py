"""
Invitation Handlers for Watchtower News
"""
from handlers.base import JsonAuthHandler
from logic.invitation import get_invitation, get_invitations, post_invitation_is_active, delete_invitation, \
    post_invitation

__author__ = 'Enis Simsar'


class InvitationHandler(JsonAuthHandler):
    def data_received(self, chunk):
        pass

    def get(self, invitation_id=None):
        if invitation_id:
            self.response = get_invitation(self.user_id, invitation_id)
        else:
            self.response = get_invitations(self.user_id)

        self.write_json()

    def post(self):
        self.response = post_invitation(self.user_id)
        self.write_json()

    def put(self, invitation_id):
        if 'status' not in self.request.arguments:
            self.response = {'error': 'status is required!'}
            self.write_json()
            return

        status = self.request.arguments['status']
        self.response = post_invitation_is_active(self.user_id, invitation_id, status)
        self.write_json()

    def delete(self, invitation_id):
        self.response = delete_invitation(self.user_id, invitation_id)
        self.write_json()
