from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_cause import AlertCause
from ..models.alert_effect import AlertEffect
from ..models.alert_severity_level import AlertSeverityLevel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.time_range import TimeRange


T = TypeVar("T", bound="Alert")


@_attrs_define
class Alert:
    """An alert, indicating some sort of incident in the public transit network.

    Attributes:
        header_text (str): Header for the alert. This plain-text string will be highlighted, for example in boldface.
        description_text (str): Description for the alert.
            This plain-text string will be formatted as the body of the alert (or shown on an explicit "expand" request by
            the user).
            The information in the description should add to the information of the header.
        code (str | Unset): Attribute or notice code (e.g. for HRDF or NeTEx)
        communication_period (list[TimeRange] | Unset): Time when the alert should be shown to the user.
            If missing, the alert will be shown as long as it appears in the feed.
            If multiple ranges are given, the alert will be shown during all of them.
        impact_period (list[TimeRange] | Unset): Time when the services are affected by the disruption mentioned in the
            alert.
        cause (AlertCause | Unset): Cause of this alert.
        cause_detail (str | Unset): Description of the cause of the alert that allows for agency-specific language;
            more specific than the Cause.
        effect (AlertEffect | Unset): The effect of this problem on the affected entity.
        effect_detail (str | Unset): Description of the effect of the alert that allows for agency-specific language;
            more specific than the Effect.
        url (str | Unset): The URL which provides additional information about the alert.
        tts_header_text (str | Unset): Text containing the alert's header to be used for text-to-speech implementations.
            This field is the text-to-speech version of header_text.
            It should contain the same information as headerText but formatted such that it can read as text-to-speech
            (for example, abbreviations removed, numbers spelled out, etc.)
        tts_description_text (str | Unset): Text containing a description for the alert to be used for text-to-speech
            implementations.
            This field is the text-to-speech version of description_text.
            It should contain the same information as description_text but formatted such that it can be read as text-to-
            speech
            (for example, abbreviations removed, numbers spelled out, etc.)
        severity_level (AlertSeverityLevel | Unset): The severity of the alert.
        image_url (str | Unset): String containing an URL linking to an image.
        image_media_type (str | Unset): IANA media type as to specify the type of image to be displayed. The type must
            start with "image/"
        image_alternative_text (str | Unset): Text describing the appearance of the linked image in the image field
            (e.g., in case the image can't be displayed or the user can't see the image for accessibility reasons).
            See the HTML spec for alt image text.
    """

    header_text: str
    description_text: str
    code: str | Unset = UNSET
    communication_period: list[TimeRange] | Unset = UNSET
    impact_period: list[TimeRange] | Unset = UNSET
    cause: AlertCause | Unset = UNSET
    cause_detail: str | Unset = UNSET
    effect: AlertEffect | Unset = UNSET
    effect_detail: str | Unset = UNSET
    url: str | Unset = UNSET
    tts_header_text: str | Unset = UNSET
    tts_description_text: str | Unset = UNSET
    severity_level: AlertSeverityLevel | Unset = UNSET
    image_url: str | Unset = UNSET
    image_media_type: str | Unset = UNSET
    image_alternative_text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        header_text = self.header_text

        description_text = self.description_text

        code = self.code

        communication_period: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.communication_period, Unset):
            communication_period = []
            for communication_period_item_data in self.communication_period:
                communication_period_item = communication_period_item_data.to_dict()
                communication_period.append(communication_period_item)

        impact_period: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.impact_period, Unset):
            impact_period = []
            for impact_period_item_data in self.impact_period:
                impact_period_item = impact_period_item_data.to_dict()
                impact_period.append(impact_period_item)

        cause: str | Unset = UNSET
        if not isinstance(self.cause, Unset):
            cause = self.cause.value

        cause_detail = self.cause_detail

        effect: str | Unset = UNSET
        if not isinstance(self.effect, Unset):
            effect = self.effect.value

        effect_detail = self.effect_detail

        url = self.url

        tts_header_text = self.tts_header_text

        tts_description_text = self.tts_description_text

        severity_level: str | Unset = UNSET
        if not isinstance(self.severity_level, Unset):
            severity_level = self.severity_level.value

        image_url = self.image_url

        image_media_type = self.image_media_type

        image_alternative_text = self.image_alternative_text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "headerText": header_text,
                "descriptionText": description_text,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if communication_period is not UNSET:
            field_dict["communicationPeriod"] = communication_period
        if impact_period is not UNSET:
            field_dict["impactPeriod"] = impact_period
        if cause is not UNSET:
            field_dict["cause"] = cause
        if cause_detail is not UNSET:
            field_dict["causeDetail"] = cause_detail
        if effect is not UNSET:
            field_dict["effect"] = effect
        if effect_detail is not UNSET:
            field_dict["effectDetail"] = effect_detail
        if url is not UNSET:
            field_dict["url"] = url
        if tts_header_text is not UNSET:
            field_dict["ttsHeaderText"] = tts_header_text
        if tts_description_text is not UNSET:
            field_dict["ttsDescriptionText"] = tts_description_text
        if severity_level is not UNSET:
            field_dict["severityLevel"] = severity_level
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url
        if image_media_type is not UNSET:
            field_dict["imageMediaType"] = image_media_type
        if image_alternative_text is not UNSET:
            field_dict["imageAlternativeText"] = image_alternative_text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.time_range import TimeRange

        d = dict(src_dict)
        header_text = d.pop("headerText")

        description_text = d.pop("descriptionText")

        code = d.pop("code", UNSET)

        _communication_period = d.pop("communicationPeriod", UNSET)
        communication_period: list[TimeRange] | Unset = UNSET
        if _communication_period is not UNSET:
            communication_period = []
            for communication_period_item_data in _communication_period:
                communication_period_item = TimeRange.from_dict(communication_period_item_data)

                communication_period.append(communication_period_item)

        _impact_period = d.pop("impactPeriod", UNSET)
        impact_period: list[TimeRange] | Unset = UNSET
        if _impact_period is not UNSET:
            impact_period = []
            for impact_period_item_data in _impact_period:
                impact_period_item = TimeRange.from_dict(impact_period_item_data)

                impact_period.append(impact_period_item)

        _cause = d.pop("cause", UNSET)
        cause: AlertCause | Unset
        if isinstance(_cause, Unset):
            cause = UNSET
        else:
            cause = AlertCause(_cause)

        cause_detail = d.pop("causeDetail", UNSET)

        _effect = d.pop("effect", UNSET)
        effect: AlertEffect | Unset
        if isinstance(_effect, Unset):
            effect = UNSET
        else:
            effect = AlertEffect(_effect)

        effect_detail = d.pop("effectDetail", UNSET)

        url = d.pop("url", UNSET)

        tts_header_text = d.pop("ttsHeaderText", UNSET)

        tts_description_text = d.pop("ttsDescriptionText", UNSET)

        _severity_level = d.pop("severityLevel", UNSET)
        severity_level: AlertSeverityLevel | Unset
        if isinstance(_severity_level, Unset):
            severity_level = UNSET
        else:
            severity_level = AlertSeverityLevel(_severity_level)

        image_url = d.pop("imageUrl", UNSET)

        image_media_type = d.pop("imageMediaType", UNSET)

        image_alternative_text = d.pop("imageAlternativeText", UNSET)

        alert = cls(
            header_text=header_text,
            description_text=description_text,
            code=code,
            communication_period=communication_period,
            impact_period=impact_period,
            cause=cause,
            cause_detail=cause_detail,
            effect=effect,
            effect_detail=effect_detail,
            url=url,
            tts_header_text=tts_header_text,
            tts_description_text=tts_description_text,
            severity_level=severity_level,
            image_url=image_url,
            image_media_type=image_media_type,
            image_alternative_text=image_alternative_text,
        )

        alert.additional_properties = d
        return alert

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
