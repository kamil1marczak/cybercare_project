from fastapi import APIRouter

from fastapi.encoders import jsonable_encoder

from service_client.web.api.event.schema import Event
from service_client.web.utils import write_output_to_json

router = APIRouter()

@router.post("/", response_model=Event)
async def send_echo_message(
    incoming_message: Event,
) -> Event:
    """
    Sends echo back to user.

    :param incoming_message: incoming message.
    :returns: message same as the incoming.
    """
    json_compatible_incoming_message = jsonable_encoder(incoming_message)
    write_output_to_json(json_compatible_incoming_message)

    return incoming_message
