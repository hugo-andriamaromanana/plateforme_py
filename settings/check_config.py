import sys

from forms_sender import Profile
from settings.consts import (
    SEND_MULTIPLE_PROFILES,
    SEND_PROFILE,
    EMAIL,
    FIRST_NAME,
    LAST_NAME,
    URL,
    URLS,
    PROFILES,
    PROFILE,
    AUTO,
)
from settings.config import (
    PARAMS,
    CONFIG_PATH,
    LOGS_PATH,
    DEFAULT_PARAMS,
    LAST_LOGS,
    write_to_json,
)


class Checker:
    def config_check(self):
        if self._check_empty_config():
            self._define_is_single()
            if not (self._check_no_mails(self.is_single)):
                print("[error] missing an email adress")
                sys.exit(0)
            print("[done] config is valid")
            return True
        sys.exit(0)

    def _define_is_single(self) -> bool:
        log_single: bool = self._check_no_config(is_single=True)
        log_multiple: bool = self._check_no_config(is_single=False)
        if log_multiple ^ log_single:
            self.is_single: bool = log_single
            print("[detected] single send") if self.is_single else print(
                "[detected] multiple sends"
            )

        else:
            print(f"[error] something is wrong\nYOUR SETTINGS:{PARAMS}")
            print("[reset] invalid format file")
            sys.exit(0)

    def _check_no_config(self, is_single: bool) -> list:
        door: str = SEND_PROFILE if is_single else SEND_MULTIPLE_PROFILES
        return not (PARAMS[door] == DEFAULT_PARAMS[door])

    def _generate_for_single(self):
        send_profile: str = PARAMS[SEND_PROFILE]
        profile_dic: dict = send_profile[PROFILE]
        url: str = send_profile[URL]
        email: str = profile_dic[EMAIL]
        first_name: str = profile_dic[FIRST_NAME]
        last_name: str = profile_dic[LAST_NAME]
        is_auto: bool = profile_dic[AUTO]

        profile: Profile = Profile(
            auto_generate_name=is_auto,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )

        return profile, url

    def _check_no_mails(self, is_single: bool) -> bool:
        if not (is_single):
            all_profiles: list[str] = PARAMS[SEND_MULTIPLE_PROFILES][PROFILES]
            multiple_mails: list[str] | list[None] = [
                all_profiles[index].get(EMAIL) for index in range(len(all_profiles))
            ]
            return multiple_mails[0] is not None
        single_mail: str | None = PARAMS[SEND_PROFILE][PROFILE].get(EMAIL)
        return single_mail != ""

    def _generate_for_multiple(self):
        profiles: list = []
        urls: list = []
        send_profiles: list[dict] = PARAMS[SEND_MULTIPLE_PROFILES][PROFILES]
        for tag in send_profiles:
            first_name: str = tag.get(FIRST_NAME)
            last_name: str = tag.get(LAST_NAME)
            email: str = tag.get(EMAIL)
            is_auto: str = tag.get(AUTO)
            profiles.append(
                Profile(
                    auto_generate_name=is_auto,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                )
            )
            urls: str = PARAMS[SEND_MULTIPLE_PROFILES][URLS]
        return profiles, urls

    def save_logs(self, new_logs: dict):
        last_logs: list = LAST_LOGS
        last_logs.append(new_logs)
        write_to_json(last_logs, LOGS_PATH)

    def reset_config(self):
        write_to_json(DEFAULT_PARAMS, CONFIG_PATH)
        print(f"[reset] config reset")

    def _check_empty_config(self):
        if not (PARAMS == DEFAULT_PARAMS):
            return True
        print("[error] The config file is empty")
        sys.exit(0)
