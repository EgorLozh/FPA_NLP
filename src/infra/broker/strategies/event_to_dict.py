from src.domain.events.base import BaseEvent
from src.domain.events.events import ComplitedReport
from src.infra.broker.schemas import ReportMessageSchema, ReportSchema, CheckedScriptActionSchema
from src.infra.broker.strategies.base import BaseEventToDictStrategy


class ComplitedReportToDictStrategy(BaseEventToDictStrategy):
    @staticmethod
    def event_to_dict(event: ComplitedReport) -> dict:
        script_actions = [
            CheckedScriptActionSchema(
            text=mark.script_action.text,
            weight=mark.script_action.weight,
            check=mark.check) 
            for mark in event.report.marks]
        report = ReportSchema(
            request_id=event.report.request.oid,
            total_score=event.report.total_score,
            actions=script_actions
        )
        
        return ReportMessageSchema(type="report", data=report).model_dump()
