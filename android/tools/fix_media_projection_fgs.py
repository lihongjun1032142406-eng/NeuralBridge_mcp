from pathlib import Path

p = Path('android/app/src/main/kotlin/com/neuralbridge/companion/service/NeuralBridgeAccessibilityService.kt')
s = p.read_text(encoding='utf-8')
old = 'startForeground(NOTIFICATION_ID, notification, ServiceInfo.FOREGROUND_SERVICE_TYPE_SPECIAL_USE)'
new = '''startForeground(
                NOTIFICATION_ID,
                notification,
                ServiceInfo.FOREGROUND_SERVICE_TYPE_SPECIAL_USE or
                    ServiceInfo.FOREGROUND_SERVICE_TYPE_MEDIA_PROJECTION
            )'''
if old not in s:
    raise SystemExit('expected Android 14+ startForeground call not found')
s = s.replace(old, new, 1)
p.write_text(s, encoding='utf-8')

manifest = Path('android/app/src/main/AndroidManifest.xml').read_text(encoding='utf-8')
required = [
    'android.permission.FOREGROUND_SERVICE_MEDIA_PROJECTION',
    'android:foregroundServiceType="specialUse|mediaProjection"',
]
for token in required:
    if token not in manifest:
        raise SystemExit(f'missing required manifest declaration: {token}')

print('MediaProjection FGS FIX1 applied and manifest prerequisites verified')
