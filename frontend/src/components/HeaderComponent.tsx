import {Burger, Group, Image, Title} from "@mantine/core";
import {useDisclosure} from "@mantine/hooks";
import logo from "../assets/blobnom.png"

const HeaderComponent = () => {
    const [opened, {toggle}] = useDisclosure();

    return (
        <Group h="100%" px="md">
            <Burger
                opened={opened}
                onClick={toggle}
                hiddenFrom="sm"
                size="sm"
            />

            <Image py="sm" h="100%" src={logo}/>
            <a href="/" className="no-underline text-white">
                <Title order={4}>Blobnom</Title>
            </a>
        </Group>
    );
};

export default HeaderComponent;
