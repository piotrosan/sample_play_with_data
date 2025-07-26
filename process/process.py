class AbstractProcess:

    _ordered_steps = None
    _result = None

    def build_step(self, step, *args):
        if self._ordered_steps is not None:
            self._ordered_steps.append({
                'step': step,
                'args': args
            })
        else:
            self._ordered_steps = [{
                'step': step,
                'args': args
            }]

    def run_process(self):
        self._result = []
        for step_with_args in self._ordered_steps:
            self._result.append(
                step_with_args['step'](*step_with_args['args'])
            )

    def get_result(self):
        return self._result


class AbstractPipeline:

    _ordered_steps = None
    _first_args = None
    _result = None

    def build_step(self, step, *args):
        self._first_args = args
        if self._ordered_steps is not None:
            self._ordered_steps.append(step)
        else:
            self._ordered_steps = [step]

    def run_pipeline(self):
        self._result = None
        for inx, step_with_args in enumerate(self._ordered_steps):
            if inx == 0:
                self._result = step_with_args[inx]['step'](self._first_args)
            else:
                self._result = step_with_args[inx](self._result)

    def get_result(self):
        return self._result
