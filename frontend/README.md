# Frontend

Expo (SDK 57) + Expo Router + TypeScript.

## Run

```bash
cp .env.example .env   # set EXPO_PUBLIC_API_URL to the backend
npm install
npm start              # scan the QR code with Expo Go
```

`npm run typecheck`, `npm run lint`, `npm run doctor`.

Add packages with `npx expo install <pkg>`, not `npm install`, so versions match the SDK.

## Layout

```
src/
├── app/            routes only (Expo Router). Files here become screens; keep logic out.
│   ├── _layout.tsx root stack + status bar
│   └── index.tsx   "/" — Hello World
├── components/     reusable UI (Screen container, AppText)
├── constants/      design tokens (colours, spacing, font sizes)
├── config/         env.ts — the only place that reads EXPO_PUBLIC_* vars
└── services/api/   client.ts — single fetch wrapper; add one file per backend resource
```

Add `hooks/` and `types/` under `src/` as you need them. Import with the `@/` alias (`@/components/Screen`).
