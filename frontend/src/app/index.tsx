import { AppText } from '@/components/AppText';
import { Screen } from '@/components/Screen';

/** Home route ("/") showing a placeholder title. */
export default function HomeScreen() {
  return (
    <Screen>
      <AppText variant="title">Hello World</AppText>
    </Screen>
  );
}
