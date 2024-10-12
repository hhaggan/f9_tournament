import { Anchor, Container, Group } from '@mantine/core';

import { BrandFooter } from '../navbar/_brand';
import classes from './footer.module.css';

const links = [
  { link: 'https://forte9.store/', label: 'Website' },
  { link: '', label: 'GitHub' },
];

export function DashboardFooter() {
  const items = links.map((link) => (
    <Anchor<'a'> c="dimmed" key={link.label} href={link.link} size="sm">
      {link.label}
    </Anchor>
  ));

  return (
    <div className={classes.footer}>
      <Container className={classes.inner}>
        <BrandFooter />
        <Group className={classes.links}>{items}</Group>
      </Container>
    </div>
  );
}
