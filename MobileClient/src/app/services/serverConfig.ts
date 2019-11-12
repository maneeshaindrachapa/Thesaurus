export class ServerConfig {
  // public host = 'http://thesaurus.projects.uom.lk';
  public host = 'http://127.0.0.1';
  public port = '5000';
  // tslint:disable-next-line:variable-name
  public base_url = this.host + ':' + this.port;
}
