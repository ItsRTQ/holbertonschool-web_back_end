import signUpUser from "./4-user-promise";
import uploadPhoto from "./5-photo-reject";
export default async function handleProfileSignup(firstName, lastName, fileName) {
  const signUpResult = await signUpUser(firstName, lastName);
  const uploadResult = await uploadPhoto(fileName);
  const data = [{
    status: signUpResult.status(),
    value: signUpResult,
  }, {
    status: uploadResult.status(),
    value: uploadResult,
  }];
}
