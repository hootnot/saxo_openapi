# -*- coding: utf-8 -*-

import struct
import json


def decode_ws_msg(raw):
    """decode a websocket message and return the decoded message.

    Since the stream may contain messages from different sources
    identified by the referenceId, the message is returned as
    a dict:

     ::

        { 'refId': '...',
            'msg': ...
         }

    The value assigned to msg can be parsed JSON data, so a dict, or
    a string.
    """
    (msgIdentifier,), raw = struct.unpack_from("Q", raw[:8]), raw[8+2:]
    # (Reserved,), raw = struct.unpack_from("h", raw[:2]), raw[2:]

    (Srefid,), raw = struct.unpack_from("B", raw[:1]), raw[1:]
    FS = "{}s".format(Srefid)
    (refid,), raw = struct.unpack_from(FS, raw[:Srefid]), raw[Srefid:]
    (payloadFmt,), raw = struct.unpack_from("B", raw[:1]), raw[1:]
    (payloadSize,), raw = struct.unpack_from("i", raw[:4]), raw[4:]

    FS = "{}s".format(payloadSize)
    (payload,) = struct.unpack_from(FS, raw[:payloadSize])

    msg = {'refid': refid,
           'msgId': msgIdentifier}

    if payloadFmt == 0:
        msg.update({'msg': json.loads(str(payload, 'utf-8'))})

    else:
        msg.update({'msg': payload})

    return msg
