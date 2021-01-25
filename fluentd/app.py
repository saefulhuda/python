from fluent import sender
from fluent import event
sender.setup('fluentd.test.log', host='127.0.0.1', port=24220)
event.Event('follow', {
  'from': 'userA',
  'to':   'userB'
})