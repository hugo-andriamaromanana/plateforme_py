import sys

from settings.config import (
    PARAMS,
    CONFIG_PATH,
    LOGS_PATH,
    DEFAULT_PARAMS,
    write_to_json,
    load_json_from_URL,
)

from forms_sender import Profile


class Checker:
    def config_check(self):
        self._empty_config()
        self._define_is_single()
        print("[done] config is valid")
        return True

    def generate_for_single(self):
        send_profile: str = PARAMS["send_profile"]
        email: str = send_profile["email"]
        first_name: str = send_profile["first_name"]
        last_name: str = send_profile["last_name"]

        self.profile: Profile = Profile(
            auto_generate_name=self.is_auto,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )

        self.url: str = send_profile["url"]

    def generate_for_multiple(self):
        self.profile = []
        send_profiles: int | list[str] = PARAMS["send_multiple_profiles"]["profiles"]
        for tag in send_profiles:
            email: str = tag
            if self.is_auto:
                first_name: str = ""
                first_name: str = ""
            else:
                first_name: str = tag["first_name"]
                last_name: str = tag["last_name"]
                self.profile.append(
                    Profile(
                        auto_generate_name=self.is_auto,
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                    )
                )
                self.url: str = PARAMS["send_multiple_profiles"]["urls"]

    def are_name_auto(self):
        is_empty_single: bool = (
            PARAMS["send_profile"]["first_name"] == ""
            and PARAMS["send_profile"]["last_name"] == ""
        )
        is_empty_multiple: bool = PARAMS["send_multiple_profiles"]["auto"] is None

        return is_empty_multiple or is_empty_single

    def save_logs(self, new_logs: dict):
        last_logs = load_json_from_URL(LOGS_PATH)
        updated_logs = last_logs.update(new_logs)
        write_to_json(updated_logs, LOGS_PATH)

    def reset_config(self):
        write_to_json(DEFAULT_PARAMS, CONFIG_PATH)

    def _empty_config(self):
        if not (PARAMS == DEFAULT_PARAMS):
            return True
        print("[error] The config file is empty")
        sys.exit(0)

    def _define_is_single(self) -> bool:
        log_single: bool = self._check_no_config(is_single=True)
        log_multiple: bool = self._check_no_config(is_single=False)
        print(f"log_multiple: {log_multiple}")
        print(f"log_single: {log_single}")
        if log_multiple ^ log_single:
            if log_single:
                self.is_auto: bool = (
                    PARAMS["send_profile"]["first_name"] == ""
                    and PARAMS["send_profile"]["last_name"] == ""
                )
                print("[detected] single send")
            else:
                self.is_auto: bool = PARAMS["send_multiple_profiles"]["auto"] is None
                print("[detected] multiple sends")
            self.is_single: bool = log_single
            print(self.is_single)
        else:
            print(f"[error] something is wrong\nYOUR SETTINGS:{PARAMS}")
            print("[reset] invalid format file")
            sys.exit(0)

    def _check_no_config(self, is_single: bool) -> list:
        door: str = "send_profile" if is_single else "send_multiple_profiles"
        return not(PARAMS[door] == DEFAULT_PARAMS[door])
